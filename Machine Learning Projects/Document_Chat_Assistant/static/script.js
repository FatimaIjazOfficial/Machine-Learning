const API_URL = "http://localhost:5500";
const uploadZone = document.getElementById("uploadZone");
const fileInput = document.getElementById("fileInput");

uploadZone.addEventListener("click", () => {
    fileInput.click();
});

uploadZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadZone.classList.add("dragover");
});

uploadZone.addEventListener("dragleave", () => {
    uploadZone.classList.remove("dragover");
});

uploadZone.addEventListener("drop", async (e) => {
    e.preventDefault();
    uploadZone.classList.remove("dragover");
    const files = [...e.dataTransfer.files];
    if (files.length === 0) return;
    for (const file of files) {
        await handleFileUpload(file);
    }
});

fileInput.addEventListener("change", async (e) => {
    const files = [...e.target.files];
    if (files.length === 0) return;
    for (const file of files) {
        await handleFileUpload(file);
    }
    fileInput.value = "";
});

async function handleFileUpload(file){
    const formData = new FormData();
    formData.append("file", file);
    showStatus(`Uploading ${file.name}...`, "info");
    try{
        const response = await fetch(`${API_URL}/upload`,{
            method:"POST",
            body:formData
        });
        const data = await response.json();
        if(response.ok){
            showStatus(`✅ ${data.filename} uploaded successfully.`,"success");
            await loadDocuments();
        }else{
            showStatus(`❌ ${data.error}`,"error");
        }
    }catch(error){
        showStatus(error.message,"error");
    }
}

async function loadDocuments(){
    try{
        const response = await fetch(`${API_URL}/documents`);
        const data = await response.json();
        const container=document.getElementById("documentsList");
        if(data.documents.length===0){
            container.innerHTML=`
                <div class="empty-state">
                    <div class="empty-icon">📁</div>
                    <h4>No Documents</h4>
                    <p>Upload PDF or TXT files to begin chatting.</p>
                </div>
            `;
            return;
        }
        container.innerHTML=data.documents.map(doc=>`
            <div class="document-item">
                <div class="document-left">
                    <div class="document-icon">
                        📄
                    </div>
                    <div>
                        <div class="document-name">
                            ${doc.name}
                        </div>
                        <div class="document-size">
                            ${formatBytes(doc.size)}
                        </div>
                        <div class="document-status">
                            ✅ Indexed
                        </div>
                    </div>
                </div>
                <button
                    class="delete-btn"
                    onclick="deleteDocument('${doc.name}')"
                >
                    🗑
                </button>
            </div>
        `).join("");
    }catch(error){
        console.log(error);
    }
}

async function deleteDocument(filename){
    if(!confirm(`Delete ${filename}?`)){
        return;
    }
    try{
        const response = await fetch(
            `${API_URL}/delete/${filename}`,
            {
                method:"DELETE"
            }
        );
        const data = await response.json();
        if(response.ok){
            showStatus(data.message,"success");
            loadDocuments();
        }else{
            showStatus(data.error,"error");
    }
    }catch(error){
        showStatus(error.message,"error");
    }
}

async function clearAllDocuments(){
    if(!confirm("Delete all uploaded documents?")){
        return;
    }
    try{
        const response = await fetch(`${API_URL}/clear`,{
            method:"POST"
        });
        const data = await response.json();
        if(response.ok){
            showStatus(data.message,"success");
            loadDocuments();
            document.getElementById("messages").innerHTML=`
                <div class="message assistant">
                    <div class="avatar">
                        🤖
                    </div>
                    <div class="bubble">
                        <div class="sender">
                            Assistant
                        </div>
                        <div class="text">
                            Upload one or more documents and ask me anything.
                        </div>
                    </div>
                </div>
            `;
        }else{
            showStatus(data.error,"error");
        }
    }catch(error){
        showStatus(error.message,"error");
    }
}

async function askQuestion(){
    const input=document.getElementById("questionInput");
    const question=input.value.trim();
    if(!question){
        return;
    }
    addMessage(question,"user");
    input.value="";
    const button=document.getElementById("askBtn");
    button.disabled=true;
    button.innerHTML=`<div class="loading"></div>`;
    try{
        const response=await fetch(`${API_URL}/query`,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                question:question
            })
        });
        const data=await response.json();
        if(response.ok){
            addMessage(
                data.answer,
                "assistant",
                data.sources
            );
        }else{
            addMessage(
                `❌ ${data.error}`,
                "assistant"
            );
        }
    }catch(error){
        addMessage(
            error.message,
            "assistant"
        );
    }finally{
        button.disabled=false;
        button.innerHTML="➜";
    }
}

function addMessage(content,sender,sources=[]){
    const messages=document.getElementById("messages");
    const div=document.createElement("div");
    div.className=`message ${sender}`;
    const avatar=sender==="user" ? "👤" : "🤖";
    const title=sender==="user" ? "You" : "Assistant";
    let sourceHTML="";
    if(sources && sources.length>0){
        sourceHTML=`
            <div class="sources">
                📚 Sources:
                ${[...new Set(sources)].join(", ")}
            </div>
        `;
    }
    div.innerHTML=`
        <div class="avatar">
            ${avatar}
        </div>
        <div class="bubble">
            <div class="sender">
                ${title}
            </div>
            <div class="text">
                ${content}
            </div>
            ${sourceHTML}
        </div>
    `;
    messages.appendChild(div);
    messages.scrollTop=messages.scrollHeight;
}

function handleKeyPress(event){
    if(event.key==="Enter"){
        askQuestion();
    }
}

function showStatus(message,type){
    const status=document.getElementById("status");
    status.className=`status ${type}`;
    status.textContent=message;
    status.style.display="block";
    setTimeout(()=>{
        status.style.display="none";
    },4000);
}

function formatBytes(bytes){
    if(bytes===0){
        return "0 Bytes";
    }
    const k=1024;
    const sizes=["Bytes","KB","MB","GB"];
    const i=Math.floor(Math.log(bytes)/Math.log(k));
    return (
        Math.round((bytes/Math.pow(k,i))*100)/100+
        " "+
        sizes[i]
    );
}

window.addEventListener("load",()=>{
    loadDocuments();
});