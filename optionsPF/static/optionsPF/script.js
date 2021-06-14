function bid_ask() {
    let table = document.getElementsByClassName("call-table")
    let selected_strike = document.getElementsByClassName("strikeClass")[0].value
    let result = null
    for (let i = 0; i < table[0].children[1].childNodes.length; i++) {
        let strike_price = document.querySelector("body > form > table.call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(1)")
        if (strike_price !== null && strike_price.childNodes[0].data === selected_strike) {
            let last_price = document.querySelector("body > form > table.call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(2)").childNodes[0].data
            let bid = document.querySelector("body > form > table.call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(3)").childNodes[0].data
            let ask = document.querySelector("body > form > table.call-table > tbody > tr:nth-child(" + i + ") > td:nth-child(4)").childNodes[0].data
            result = {
                strike: selected_strike,
                last_price: last_price,
                bid: bid,
                ask: ask
            }
        }
    }
    console.log(result)
    let url = document.getElementsByClassName("url-covered-call")[0].attributes[0].value
    $.ajax({
        type: "GET",
        url: url,
        data: {
            "result": result,
        },
        dataType: "json",
        success: function (data) {
            // any process in data
            alert("success")
        },
        failure: function () {
            alert("failure");
        }
    });
}
