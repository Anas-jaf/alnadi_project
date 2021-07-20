const typingDiv = document.getElementById('typing');
console.log(typingDiv);

// const text = "The Spring Framework is an application framework and inversion of control container for the Java platform. The framework's core features can be used by any Java application, but there are extensions for building web applications on top of the Java EE"
const text = "هذا النص هو مثال لنص يمكن أن يستبدل في نفس المساحة، لقد تم توليد هذا النص من مولد النص العربى، حيث يمكنك أن تولد مثل هذا النص أو العديد من النصوص الأخرى إضافة"

const startGame = () =>{

    startGameBtn.classList.add('hidden');


    const charachters = text.split('').map(char => {
    const span= document.createElement('span');
    span.innerText = char;
    typingDiv.appendChild(span);
    return span;
    });

    let cursorIndex = 0;
    let cursorCharacter = charachters[cursorIndex];
    cursorCharacter.classList.add ("cursor");


    let startTime = null;
    let endTime =null;

    const keylistener = document.addEventListener("keydown" , ({ key }) => {  
        console.log(key);
        if (!startTime){
            startTime=new Date();

        }
        if (key === cursorCharacter.innerText) {
        //we typed the correct color
        cursorCharacter.classList.remove("cursor");
        cursorCharacter.classList.add("done");
        cursorCharacter = charachters[++cursorIndex];
        }
        else if(key === "Backspace"){
            if (cursorIndex > 0){
            cursorCharacter.classList.remove("cursor");
            cursorCharacter.classList.remove("done");
            cursorCharacter.classList.remove("wrong");
            cursorCharacter.classList.add("fixed");
            cursorCharacter = charachters[--cursorIndex];
            }
        }
        
        else{
            cursorCharacter.classList.remove("cursor");
            cursorCharacter.classList.add("wrong");
            cursorCharacter = charachters[++cursorIndex];
        }
        // calculate wpm
        if (cursorIndex >= charachters.length){
            endTime=new Date();
            const delta = endTime - startTime;
            const seconds = delta /1000;
            const numberOfWords = text.split(" ").length
            const wps = numberOfWords/seconds ;
            const wpm =wps *60.0
            document.getElementById('stats').innerText=`wpm = ${wpm}`
            // display the wpm,cpm
            document.removeEventListener("keydown" , keylistener);
            startGameBtn.classList.remove("hidden");
            return;
        }

        cursorCharacter.classList.add("cursor");
    });

}
// add timer for charachters in word 
