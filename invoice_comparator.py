import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2
from rapidfuzz import fuzz
from pdf2image import convert_from_path
import os


def extractTextFromPdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def extractLayoutFeatures(file_path):
    layout_features = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    layout_features.extend(table)
    return layout_features


def calculateCosineSimilarity(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2]).toarray()
    return cosine_similarity(vectors)[0, 1]


def flattenFeature(feature):
    flattened = []
    for sublist in feature:
        for item in sublist:
            if item:
                flattened.append(str(item))
    return " ".join(flattened)


def calculateLevenshteinSimilarity(feature1, feature2):
    flattened1 = flattenFeature(feature1)
    flattened2 = flattenFeature(feature2)
    return fuzz.ratio(flattened1, flattened2) / 100


def convertPdfToImage(pdf_path):
    images = convert_from_path(pdf_path)
    return np.array(images[0])


def calculateStructuralSimilarity(pdf1_path, pdf2_path):
    img1 = convertPdfToImage(pdf1_path)
    img2 = convertPdfToImage(pdf2_path)
    if len(img1.shape) == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    if len(img2.shape) == 3:
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    min_height = min(img1.shape[0], img2.shape[0])
    min_width = min(img1.shape[1], img2.shape[1])
    return ssim(img1[:min_height, :min_width], img2[:min_height, :min_width])


def combineScores(text_similarity, layout_similarity, levenshtein_similarity, weights=(0.4, 0.4, 0.2)):
    weighted_scores = (text_similarity * weights[0], layout_similarity * weights[1], levenshtein_similarity * weights[2])
    return sum(weighted_scores)


def compareInvoiceToDatabase(input_invoice, database_invoices):
    print(f"Comparing invoice: {input_invoice}")
    input_text = extractTextFromPdf(input_invoice)
    input_layout_features = extractLayoutFeatures(input_invoice)
    scores = []
    for db_invoice in database_invoices:
        db_text = extractTextFromPdf(db_invoice["file_path"])
        db_layout_features = extractLayoutFeatures(db_invoice["file_path"])
        text_similarity = calculateCosineSimilarity(input_text, db_text)
        layout_similarity = calculateStructuralSimilarity(input_invoice, db_invoice["file_path"])
        levenshtein_similarity = calculateLevenshteinSimilarity(input_layout_features, db_layout_features)
        total_score = combineScores(text_similarity, layout_similarity, levenshtein_similarity)
        scores.append({"file_path": db_invoice["file_path"], "score": total_score})

    scores.sort(key=lambda x: x["score"], reverse=True)
    print("\n--- Comparison Results ---\n")
    for idx, score in enumerate(scores, start=1):
        file_name = score['file_path'].split('/')[-1]
        print(f"{idx}. Invoice Name: {file_name}")
        print(f"   Similarity Score: {score['score']}")
        print("__________________________")


def get_invoice_paths(directory):
    return [{"file_path": os.path.join(directory, f)} for f in os.listdir(directory) if f.lower().endswith('.pdf')]


def main():
    import sys
    if len(sys.argv) == 1:
        database_directory = input("Enter the directory path containing database invoices: ")
        input_invoice = input("Enter the path of the invoice to compare: ")
    elif len(sys.argv) == 2 and sys.argv[1] == '--help':
        print("Usage:\n------")
        print("To run the module from the terminal and interactively provide invoice paths:")
        print("$ python invoice_comparator.py")
        print("\nTo run the module from the terminal by providing invoice paths as arguments:")
        print("$ python invoice_comparator.py <database_directory> <input_invoice_path>")
        return
    else:
        database_directory = sys.argv[1]
        input_invoice = sys.argv[2]

    database_invoices = get_invoice_paths(database_directory)
    compareInvoiceToDatabase(input_invoice, database_invoices)


if __name__ == "__main__":
    main()

"""
Usage:
------
To run the module from the terminal and interactively provide invoice paths:
$ python invoice_comparator.py

To run the module from the terminal by providing invoice paths as arguments:
$ python invoice_comparator.py <database_directory> <input_invoice_path>
"""
