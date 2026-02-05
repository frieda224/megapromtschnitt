<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Zeugnisschnitt Rechner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            padding: 20px;
        }

        h1 {
            text-align: center;
        }

        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
        }

        .row {
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
        }

        input {
            flex: 1;
            padding: 8px;
        }

        button {
            padding: 8px 12px;
            cursor: pointer;
        }

        .result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Zeugnisschnitt Rechner</h1>

    <label>
        Notensystem:
        <select id="system" onchange="berechnen()">
            <option value="noten">Noten (1–6)</option>
            <option value="punkte">Punkte (0–15)</option>
        </select>
    </label>

    <div id="faecher"></div>

    <button onclick="fachHinzufuegen()">Fach hinzufügen</button>

    <div class="result" id="ergebnis">
        Durchschnitt: –
    </div>
</div>

<script>
    function fachHinzufuegen() {
        const container = document.getElementById("faecher");

        const row = document.createElement("div");
        row.className = "row";

        const fach = document.createElement("input");
        fach.placeholder = "Fachname";

        const note = document.createElement("input");
        note.type = "number";
        note.placeholder = "Note / Punkte";
        note.oninput = berechnen;

        const loeschen = document.createElement("button");
        loeschen.textContent = "X";
        loeschen.onclick = () => {
            row.remove();
            berechnen();
        };

        row.appendChild(fach);
        row.appendChild(note);
        row.appendChild(loeschen);

        container.appendChild(row);
    }

    function berechnen() {
        const system = document.getElementById("system").value;
        const notenFelder = document.querySelectorAll("#faecher input[type='number']");

        let summe = 0;
        let anzahl = 0;

        notenFelder.forEach(feld => {
            const wert = parseFloat(feld.value);

            if (!isNaN(wert)) {
                if (
                    (system === "noten" && wert >= 1 && wert <= 6) ||
                    (system === "punkte" && wert >= 0 && wert <= 15)
                ) {
                    summe += wert;
                    anzahl++;
                }
            }
        });

        const ergebnis = document.getElementById("ergebnis");

        if (anzahl === 0) {
            ergebnis.textContent = "Durchschnitt: –";
        } else {
            const durchschnitt = (summe / anzahl).toFixed(2);
            ergebnis.textContent = "Durchschnitt: " + durchschnitt;
        }
    }

    // Start mit einem Fach
    fachHinzufuegen();
</script>

</body>
</html>
