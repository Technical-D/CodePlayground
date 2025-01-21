const editor = CodeMirror.fromTextArea(document.getElementById("code-editor"), {
    mode: "python", 
    theme: "dracula",
    lineNumbers: false, 
    lineWrapping: true, 
    matchBrackets: true,
    autoCloseBrackets: true, 
    indentUnit: 4, 
    fontSize: "16px",
});

// Run Code
async function runCode() {
    const code = editor.getValue();
    const spinner = document.getElementById('spinner');
    spinner.classList.remove('hidden');
    try{
        const response = await fetch('/python/run', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code: code })
        });
        const result = await response.json();
        document.getElementById('output').innerText = result.output + result.error;
    } catch (error){
        outputElement.innerText = "An error occurred while running the code.";
        console.error(error);
    } finally{
        spinner.classList.add('hidden');
    }
    
}
// Clear Output
function clearOutput() {
    document.getElementById("output").textContent = "";
}
