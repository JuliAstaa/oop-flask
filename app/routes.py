# import semua libraries
from flask import Blueprint, request, redirect, render_template, url_for, flash
from .models import Contact
from . import db
from sqlalchemy.exc import IntegrityError
from app.utils.validators import validate_contact

main = Blueprint('main', __name__)

# test
@main.route("/")
def index():

    contacts = Contact.query.all()

    return render_template("index.html", contacts=contacts)

@main.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        nama: str = request.form['nama'].strip()
        no_hp: str = request.form['no_hp'].strip()
        email: str = request.form['email'].strip()

        # validator
        errors: list = validate_contact(nama=nama, no_hp=no_hp, email=email)
        if errors:
            for err in errors:
                flash(err, "failed")
                return redirect(url_for('main.add'))

        else:
            new_user: Contact = Contact(name=nama, no_hp=no_hp, email=email)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash("Berhasil menambahkan data", "success")
                return redirect(url_for('main.index'))
            except IntegrityError:
                db.session.rollback()
                flash("Data dengan email / no HP itu sudah ada!", "failed")
                return redirect(url_for('main.add'))
            except Exception as e:
                db.session.rollback()
                flash(f"Gagal menambahkan data: {e}", "failed")
                return redirect(url_for('main.index'))

    return render_template("add.html")

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # dapatkan 1 user sesuai dengan id
    user = Contact.query.get_or_404(id)

    # ubah data
    if request.method == "POST":
        name: str = request.form['nama'].strip()
        no_hp: str = request.form['no_hp'].strip()
        email: str = request.form['email'].strip()

        # validator
        errors: list = validate_contact(nama=name, no_hp=no_hp, email=email, exclude_id= user.id)
        if errors:
            for err in errors:
                flash(err, "failed")
            return redirect(url_for('main.edit', id = user.id))
        else:

            user.name = name
            user.no_hp = no_hp
            user.email = email

            try:
                db.session.commit()
                flash("Berhasil edit data cihuy")
                return redirect(url_for('main.index'))
            except IntegrityError:
                db.session.rollback()
                flash("Email atau No HP sudah digunakan")
                return redirect(url_for("main.edit", id=user.id))
            except Exception as e:
                db.session.rollback()
                flash(f"Error like that shit {e}")
        
    return render_template("edit.html", user=user)

@main.route('/delete/<int:id>', methods=['GET'])

def delete(id):
    user = Contact.query.get_or_404(id)

    try:
        db.session.delete(user)
        db.session.commit()
        flash("Data berhasil dihapus")
    except:
        db.session.rollback()
        flash("Data gagal di hapus")
    
    return redirect(url_for('main.index'))
