function get_last_price() {
    let table = document.getElementById("call-table")
    let selected_strike = document.getElementById("strikeId").value
    for (let i = 0; i < table.children[1].childNodes.length; i++) {
        let strike_price = document.querySelector("#call-table > tbody > tr:nth-child("+ i +") > td:nth-child(1)")
        if (strike_price !== null && strike_price.childNodes[0].data === selected_strike) {
            let last_price = document.querySelector("#call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(2)").childNodes[0].data
            let result = document.getElementById("selected-last-price")
            result.attributes[3].value = last_price
            break
        }
    }
}