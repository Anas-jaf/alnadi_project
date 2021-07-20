
function start(){
    const typingDiv = document.getElementById('typing');
    const text = "هذا النص هو مثال لنص يمكن أن يستبدل في نفس المساحة، لقد تم توليد هذا النص من مولد النص العربى، حيث يمكنك أن تولد مثل هذا النص أو العديد من النصوص الأخرى إضافة" ;

    let charachters = text.split('').map(char => {
        const span= document.createElement('span');
        span.innerText = char;
        typingDiv.appendChild(span);
        return span;
        });

    document.getElementById("typing").innerHTML = charachters ();
 
    exports.charachters ;
}
