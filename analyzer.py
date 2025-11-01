import re
from collections import Counter

def analyze_log(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            log_data = file.readlines()

        # Define common log patterns
        error_pattern = re.compile(r'error', re.IGNORECASE)
        warning_pattern = re.compile(r'warning', re.IGNORECASE)
        info_pattern = re.compile(r'info', re.IGNORECASE)

        # Count occurrences
        error_count = sum(bool(error_pattern.search(line)) for line in log_data)
        warning_count = sum(bool(warning_pattern.search(line)) for line in log_data)
        info_count = sum(bool(info_pattern.search(line)) for line in log_data)

        # Find top repeated words
        words = re.findall(r'\b\w+\b', ''.join(log_data).lower())
        top_words = Counter(words).most_common(5)

        print("\n📊 LOG SUMMARY REPORT")
        print("-" * 45)
        print(f"Total Lines       : {len(log_data)}")
        print(f"Errors Found      : {error_count}")
        print(f"Warnings Found    : {warning_count}")
        print(f"Info Messages     : {info_count}")
        print("-" * 45)
        print("Most Frequent Words:")
        for word, count in top_words:
            print(f"  {word:<12} → {count} times")

        print("-" * 45)
        print("✅ Analysis Complete.\n")

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"⚠️ An error occurred: {str(e)}")

if __name__ == "__main__":
    file_path = "sample_logs/sample_log.txt"
    analyze_log(file_path)
