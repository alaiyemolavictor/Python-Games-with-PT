def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num    
    return total

def sum_of_odds(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

def find_palindroms(word):
    palindroms = []
    for word in word [::-1]:
        palindroms.append(word)
    return palindroms

def is_valid_email(email):
    if '@' not in email or '.' not in email:
        return False
    try:
        local, domain = email.split('@')
        domain_parts = domain.split('.')

        if len(domain_parts) != 2:
            return False

        domain_name, extension = domain_parts

        if local.isalnum() and domain_name.isalpha() and extension.isalpha():
            return True
        else:
            return False
    except:
        return False

def is_valid_phone_number(phone):
    if len(phone) != 15:
        return False
    if phone[0] != '(' or phone[6] != ')' or phone[7] != '-' or phone[11] != '-':
        return False
    if not (phone[1:6].isdigit() and phone[8:11].isdigit() and phone[12:].isdigit()):
        return False
    return True


        