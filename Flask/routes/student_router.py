from flask import Blueprint

student_bp = Blueprint("student_bp",__name__)

student_bp.add_url_rule('/',"index")
student_bp.add_url_rule('/add',"add",methods=["POST"])
student_bp.add_url_rule('/edit/<id>',"edit")
student_bp.add_url_rule('/update/<id>',"update",methods=["POST"])
student_bp.add_url_rule('/delete/<id>',"delete")
