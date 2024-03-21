import random
import string

def generate_password(length=8, include_digits=True, include_special_chars=True):
    """
    Generate a random password with the specified length and character types.
    
    Args:
        length (int): The length of the password (default is 8).
        include_digits (bool): Whether to include digits in the password (default is True).
        include_special_chars (bool): Whether to include special characters in the password (default is True).
        
    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 获取用户输入的密码长度和字符类型选项
length = int(input("Enter the length of the password: "))
include_digits = input("Include digits in the password? (yes/no): ").lower() == 'yes'
include_special_chars = input("Include special characters in the password? (yes/no): ").lower() == 'yes'

# 调用 generate_password 函数生成密码
password = generate_password(length, include_digits, include_special_chars)

# 打印生成的密码
print("Generated password:", password)
