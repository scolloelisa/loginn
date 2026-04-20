async function loggati() {

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (!username || !password) 
        return alert("Scrivi lo username e password");

    const res = await fetch(`/login?username=${username}&password=${password}`);
    const json = await res.json();

    Document.getElementById("risultato").innerText = json.messaggio;

}

document.getElementById('bottone').addEventListener('click', loggati);

//async == non legate nel tempo, asincrona.