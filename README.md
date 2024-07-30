# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```# Invoice Comparator

## Objective
The objective of this project is to compare a given input invoice to a database of existing invoices. The comparison is based on three similarity metrics:
1. Textual Similarity using Cosine Similarity of TF-IDF vectors.
2. Layout Similarity using Structural Similarity Index (SSIM) on images.
3. Content Similarity using Levenshtein Distance on extracted features.

## Approach
1. **Text Extraction**:
   - Using `pdfplumber`, extract text from the PDF files.
2. **Layout Feature Extraction**:
   - Extract tables and other layout features from the PDF files with `pdfplumber`.
3. **Image Conversion**:
   - Convert PDF pages into images using `pdf2image` and compute layout similarity using `scikit-image`'s SSIM function.
4. **Similarity Calculation**:
   - Compute the Cosine Similarity of text, Structural Similarity of layouts, and Levenshtein Similarity of extracted features.
5. **Combining Scores**:
   - Combine these similarity scores using a weighted approach to generate a final similarity score.
6. **Comparison and Ranking**:
   - Compare the input invoice against a list of database invoices and rank them based on the total similarity score.

## Installation
### Dependencies
- Python 3.x
- Required Python libraries:
  - `pdfplumber`
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```
  - `scikit-learn`
  - `scikit-image`
  - `opencv-python`
  - `rapidfuzz`
  - `pdf2image`
  - `numpy`

### Poppler
`pdf2image` requires Poppler to convert PDF into images. You need to install Poppler separately:

- **On Ubuntu**:
  ```sh
  sudo apt-get install poppler-utils
  ```

- **On macOS**:
  ```sh
  brew install poppler
  ```

- **On Windows**: Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows). Add the `bin` folder to your PATH.

### Python Libraries Installation
You can install the required Python libraries using pip:

```sh
pip install pdfplumber scikit-learn scikit-image opencv-python rapidfuzz pdf2image numpy
```

### Usage
#### Interactive Mode
Run the script without arguments for an interactive mode where you provide the paths for the database directory and the input invoice:

```sh
python invoice_comparator.py
```

#### Command-Line Arguments
Provide the paths for the database directory and the input invoice directly as arguments:

```sh
python invoice_comparator.py <database_directory> <input_invoice_path>
```

#### Help
To view the usage instructions:

```sh
python invoice_comparator.py --help
```

### Example
Place your invoices in a directory, say `invoices_db`.

Have your input invoice in a different location, say `input_invoices`.

Run the comparison:

```sh
python invoice_comparator.py invoices_db input_invoices/sample_invoice.pdf
```

### Notes
Ensure that all invoices in the database directory are PDF files.

The results will be printed in the console, showing the ranked list of invoices based on similarity scores.
```

This README provides clear installation, usage instructions, and explanations of dependencies and the objective of the project. It also highlights the requirement to install Poppler for PDF to image conversion.
```