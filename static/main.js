let table = document.querySelector("table")

websocket.addEventListener("message", (event) => {
    let parsedJson = JSON.parse(event.data)
    Object.keys(parsedJson).forEach((k) => {
        let element = table.querySelector("td." + k)
        element.textContent = parsedJson[k]
    })
})