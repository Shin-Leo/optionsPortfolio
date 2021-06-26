function get_last_price() {
    let table = document.getElementById("call-table")

    let low_strike = document.querySelector("#low_strikeId").value
    let mid_strike = document.querySelector("#mid_strikeId").value
    let high_strike = document.querySelector("#high_strikeId").value
    for (let i = 0; i < table.children[1].childNodes.length; i++) {
        let strike_price = document.querySelector("#call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(1)")
        if (strike_price !== null) {
            if (strike_price.childNodes[0].data === low_strike) {
                let last_price = document.querySelector("#call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(2)").childNodes[0].data
                let result = document.getElementById("low-selected-last-price")
                result.attributes[3].value = last_price
            } else if (strike_price.childNodes[0].data === mid_strike) {
                let last_price = document.querySelector("#call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(2)").childNodes[0].data
                let result = document.getElementById("mid-selected-last-price")
                result.attributes[3].value = last_price
            } else if (strike_price.childNodes[0].data === high_strike) {
                let last_price = document.querySelector("#call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(2)").childNodes[0].data
                let result = document.getElementById("high-selected-last-price")
                result.attributes[3].value = last_price
            }

        }
    }
}