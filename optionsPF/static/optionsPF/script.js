function bid_ask(calls) {
    let ret = null
    for (let i = 0; i < calls.count; i++) {
        if (calls[i][0] === document.getElementsByClassName("strikeClass")[0].value) {
            ret = {
            bid: calls[i][1],
            ask: calls[i][2]
            }
        }
    }
    console.log(ret)
    console.log(calls)
}