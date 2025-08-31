# import semua libraries
from flask import Blueprint, request, redirect, render_template, url_for, flash
from .models import Contact
from . import db

main = Blueprint('main', __name__)

# test
@main.route("/")
def index():

    contacts = Contact.query.all()

    return render_template("index.html", contacts=contacts)

@main.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        nama: str = request.form['nama']
        no_hp: str = request.form['no_hp']
        email: str = request.form['email']

        new_user: Contact = Contact(name=nama, no_hp=no_hp, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Berhasil menambahkan data")
            return redirect(url_for('main.index'))
        except:
            db.session.rollback()
            flash("Gagal menambahkan data")
            return redirect(url_for('main.index'))

    return render_template("add.html")

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # dapatkan 1 user sesuai dengan id
    user = Contact.query.get_or_404(id)

    # ubah data
    if request.method == "POST":
        user.name = request.form['nama']
        user.no_hp = request.form['no_hp']
        user.email = request.form['email']

        try:
            db.session.commit()
            flash("Berhasil edit data cihuy")
            return redirect(url_for('main.index'))
        except:
            db.session.rollback()
            flash("Gagal mengubah data... GET OUTTT!!!!!")
        
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
