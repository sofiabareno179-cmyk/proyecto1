from flask import Flask
app=Flask(__name__)
#ruta sobre la temperatura desde las url 
@app.route('/api/temperatura/<float:grados_c>', methods=['GET'])
def temperatura (grados_c:float)-> str:
    grados_f=(grados_c*9/5)+32
    return f"La temperatura es:{grados_f}"
if __name__=='__main__':
    app.run(debug=True)
