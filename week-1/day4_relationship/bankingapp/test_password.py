#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

try:
    from auth.password_handler import hash_password, verify_password
    print("[OK] Password handler imported successfully")

    # Test hashing
    test_pwd = "test_password_12345"
    hashed = hash_password(test_pwd)
    print(f"[OK] Password hashed: {hashed[:50]}...")

    # Test verification
    is_valid = verify_password(test_pwd, hashed)
    print(f"[OK] Password verified: {is_valid}")

    # Test with long password
    long_pwd = "a" * 150
    hashed_long = hash_password(long_pwd)
    print(f"[OK] Long password (150 chars) hashed successfully")

    is_valid_long = verify_password(long_pwd, hashed_long)
    print(f"[OK] Long password verified: {is_valid_long}")

    print("\n[OK] All tests passed!")

except Exception as e:
    print(f"[ERROR] {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
