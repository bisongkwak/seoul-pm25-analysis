import hashlib
import os

def compute_file_fingerprint(file_path):
    """Compute the MD5 fingerprint of a file."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist or is not accessible.")
    md5_hasher = hashlib.md5()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            md5_hasher.update(chunk)
    return md5_hasher.hexdigest()

def compare_file_signatures(file1, file2):
    """Compare two files based on their MD5 fingerprint."""
    fingerprint1 = compute_file_fingerprint(file1)
    fingerprint2 = compute_file_fingerprint(file2)

    result = []
    result.append(f"1번 파일 이름: {file1}")
    result.append(f"1번 파일의 해시 값: {fingerprint1}")
    result.append(f"2번 파일 이름: {file2}")
    result.append(f"2번 파일의 해시 값: {fingerprint2}")

    if fingerprint1 == fingerprint2:
        result.append("두 파일은 동일한 파일입니다.")
    else:
        result.append("두 파일은 다른 파일입니다.")
    
    print("\n".join(result))
    
    with open("hash_results.txt", "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(result))
    print("\n결과가 'hash_results.txt' 파일에 저장되었습니다.")

if __name__ == "__main__":
    file1 = input("1번 파일 이름을 넣으세요: ")
    file2 = input("2번 파일 이름을 넣으세요: ")
    try:
        compare_file_signatures(file1, file2)
    except FileNotFoundError as error:
        print(f"Error: {error}")