import re
from app.models import Contact

def validate_contact(nama: str, no_hp: str, email: str, excluding_id: int = None) -> list:
    errors: list = []

    # cek apakah field kosong
    if not nama or not no_hp or not email:
        errors.append("Semua field harus diisiii!! kimakk")

    # cek no hp
    if no_hp and not no_hp.isdigit():
        errors.append("No HP harus angka!")

    # cek duplikat
    existing_email = Contact.query.filter_by(email = email).first()
    if existing_email and existing_email.id != excluding_id:
        errors.append("Email telah digunakan!")
    
    existing_no_hp = Contact.query.filter_by(no_hp = no_hp).first()
    if existing_no_hp and existing_no_hp.id != excluding_id:
        errors.append("No HP telah digunakan!")

    return errors
