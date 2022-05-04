from flask import Flask, render_template, request
from copy import deepcopy

def determinant(matrix):
    rows = len(matrix)
    for row in matrix:
        if len(row) != rows:
            return None
    if rows == 2:
        det_2x2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det_2x2
    else:
        result = 0
        columns = rows
        for j in range(columns):
            cofactor = (-1) ** j * matrix[0][j] * determinant(smaller_matrix(matrix, 0, j))
            result += cofactor
        return result 

def smaller_matrix(matrix, row, column):
    new_matrix = deepcopy(matrix)
    new_matrix.remove(matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].remove(new_matrix[i][column])
    return new_matrix



app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def matrix():
    deter = ''
    if request.method == "POST" and "a00" in request.form and "a01" in request.form and "a02" in request.form  \
                                and "a10" in request.form and "a11" in request.form and "a12" in request.form and "a00" in request.form  \
                                and "a20" in request.form and "a21" in request.form and "a22" in request.form:
        a00 = float(request.form.get("a00"))
        a01 = float(request.form.get("a01"))
        a02 = float(request.form.get("a02"))
        a10 = float(request.form.get("a10"))
        a11 = float(request.form.get("a11"))
        a12 = float(request.form.get("a12"))
        a20 = float(request.form.get("a20"))
        a21 = float(request.form.get("a21"))
        a22 = float(request.form.get("a22"))
        matrix_3x3 = [[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]]
        deter = round(determinant(matrix_3x3), 10)
    return render_template("main.html", deter=deter)