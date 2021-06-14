function get_last_price() {
    let table = document.getElementsByClassName("call-table")
    let selected_strike = document.getElementsByClassName("strikeClass")[0].value
    for (let i = 0; i < table[0].children[1].childNodes.length; i++) {
        let strike_price = document.querySelector("body > form > table.call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(1)")
        if (strike_price !== null && strike_price.childNodes[0].data === selected_strike) {
            let last_price = document.querySelector("body > form > table.call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(2)").childNodes[0].data
            let result = document.getElementById("selected-last-price")
            result.attributes[3].value = last_price
        }
    }
}
