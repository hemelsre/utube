document.getElementById('testScriptBtn').addEventListener('click', async () => {
    const response = await fetch('/test_script');
    const data = await response.json();
    alert(`Tested Script from DB: ${data.script}`);
});