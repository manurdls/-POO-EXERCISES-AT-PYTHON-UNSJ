## Ejercicio 1

Defina una clase "Email" con los siguientes atributos: idCuenta, dominio, tipo
de dominio y contraseña (todos estos datos se ingresan por teclado). Y los
siguientes metodos:

a- El constructor, que cree una cuenta a partir de una dirección que recibe
como parámetro.

b- Método "__str__" que retorne una dirección de e-mail con los valores de los
atributos de Email. Por ejemplo:

    idCuenta:alumnopoo

    dominio:gmail

    tipoDomino:com
    
    Resultado devuelto por __str__: alumnopoo@gmail.com
    
c- Método "getDominio()", que retorne el dominio.

### Implemente un programa que permita

1- Ingresar el nombre de una persona y su dirección de e-mail, crear una
instancia de Email con el e-mail ingresado, verificar si el email no se encuentra
registrado en el archivo "archivo.csv", en ese caso, agregarlo y mostrar el
siguiente mensaje: Estimado nombre, su cuenta ha sido registrada exitosamente.
Enviaremos un correo de autentificación a la siguiente direccion: xxxxx.

2- Ingresar un e-mail y verificar si está registrado (nota: el e-mail está
registrado si se encuentra en el archivo "archivo.csv"), en caso de estarlo
cambiar su contraseña.
