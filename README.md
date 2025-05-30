# IELTS Speaking Test Platform - Module 1 Assignment

## Overview

This assignment contains:
- A Python utility script (`word_counter.py`) to count the number of words in a given text.
- A simple Flask application (`app.py`) with two routes:
  - `/` returns a greeting message.
  - `/welcome` returns a personalized welcome message in JSON format.

## File Structure

```
Module1_Assignment_Bharath-hub4/
│
├── app.py
├── word_counter.py
└── README.md
```

## 1. Python Word Counter Utility

### How to Run

```bash
python word_counter.py
```

- Enter any text when prompted.
- The script will output the original text and its word count.

### Example Usage

```
Enter some text: Hello, this is a test!
Input Text: Hello, this is a test!
Word Count: 5
```

### Edge Cases Handled

- Empty input returns count as 0.
- Text with only spaces/special characters is handled gracefully.

---

## 2. Flask Application

### Installation

Ensure you have Flask installed. If not, install it using:

```bash
pip install Flask
```

### How to Run

```bash
python app.py
```

By default, the app runs at `http://127.0.0.1:5000/`.

### Endpoints

#### `/`

- **Method:** GET
- **Description:** Returns a plain text greeting.
- **Example:**  
  Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  
  **Response:**  
  ```
  Hello, Test Taker!
  ```

#### `/welcome`

- **Method:** GET
- **Query Parameter:** `name` (string, required)
- **Description:** Returns a personalized JSON welcome message.

- **Example:**  
  Visit [http://127.0.0.1:5000/welcome?name=John](http://127.0.0.1:5000/welcome?name=John)  
  **Response:**
  ```json
  {
    "message": "Welcome to the IELTS Speaking Test, John!"
  }
  ```

##### Edge Case: Missing Name Parameter

- **Example:**  
  Visit [http://127.0.0.1:5000/welcome](http://127.0.0.1:5000/welcome)  
  **Response:**
  ```json
  {
    "error": "Missing 'name' query parameter."
  }
  ```

---

## Testing

You can use your browser or tools like `curl` or `Postman`:

```bash
curl "http://127.0.0.1:5000/welcome?name=Alice"
```

**Response:**
```json
{"message": "Welcome to the IELTS Speaking Test, Alice!"}
```

---

## Notes

- Code is well-commented for clarity.
- Handles edge cases such as missing or empty input.