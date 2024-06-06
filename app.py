from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Web</title>
    <style>
        body, html {
            width: 100%;
            height: 100%;
            padding: 0;
            margin: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(318deg, #ff0062, #ffff00, #00ff00, #00ffff, #0000ff);
            background-size: 1000% 1000%;
            -webkit-animation: Coolgradient 41s linear infinite;
            -moz-animation: Coolgradient 41s linear infinite;
            -o-animation: Coolgradient 41s linear infinite;
            animation: Coolgradient 41s linear infinite;
            text-align: center;
            padding: 20px;
            color: white;
        }

        @-webkit-keyframes Coolgradient {
            0% { background-position: 5% 0% }
            50% { background-position: 96% 100% }
            100% { background-position: 5% 0% }
        }

        @-moz-keyframes Coolgradient {
            0% { background-position: 5% 0% }
            50% { background-position: 96% 100% }
            100% { background-position: 5% 0% }
        }

        @-o-keyframes Coolgradient {
            0% { background-position: 5% 0% }
            50% { background-position: 96% 100% }
            100% { background-position: 5% 0% }
        }

        @keyframes Coolgradient {
            0% { background-position: 5% 0% }
            50% { background-position: 96% 100% }
            100% { background-position: 5% 0% }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes typing {
            0%, 100% { border-right: .15em solid transparent; }
            50% { border-right: .15em solid white; }
        }

        @keyframes out-circle-swoop {
            from {
                clip-path: var(--circle-bottom-right-in);
            }
            to {
                clip-path: var(--circle-top-right-out);
            }
        }

        [transition-style="out:custom:circle-swoop"] {
            --transition__duration: 1.25s;
            --transition__easing: cubic-bezier(.30, 1, .25, 1);
            animation-name: out-circle-swoop;
        }

        h1 {
            font-size: 3em;
            display: inline-block;
            margin-bottom: 0.5em;
            white-space: nowrap;
            overflow: hidden;
            border-right: .15em solid white;
            animation: typing 3.5s steps(30, end), fadeIn 1s;
        }

        h2 {
            font-size: 2em;
            margin-bottom: 1em;
            animation: fadeIn 2s;
        }

        a {
            display: inline-block;
            margin: 10px;
            text-decoration: none;
            color: #fff;
            background-color: #0073e6;
            padding: 10px 20px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }

        a:hover {
            background-color: #005bb5;
        }

        img {
            margin-top: 20px;
        }
    </style>
</head>
<body>
   <h2>Hola, Mi nombre es Angel Josue Hernandez Manuel</h2>
   <h3>Carrera: Ing. en Desarrollo y Gestion de Software</h3>
   <h3>Docente: Dr. Efrén Juárez Castillo</h3>
   <h3>Cruatrimestre: 9°</h3>
   <h3>Grupo: B</h3>

   <img src="static/img.jpg" alt="Imagen de Ejemplo" width="350" height="350"   >
    <p>Mis Redes Sociales</p>
   <div>
       <a href="https://www.facebook.com/profile.php?id=100018110949849" target="_blank">Facebook</a>
       <a href="https://www.instagram.com/an_gel6295/" target="_blank">Instagram</a>
   </div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
