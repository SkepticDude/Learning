import React, {useState} from 'react'

export default function TextForm(props) {
    const handleOnChange=(event)=>setText(event.target.value);
    const handleUpClick=()=>{setText(text.toUpperCase()); props.showAlert("success", "Text Converted to UPPERCASE");}
    const handleLowClick=()=>{setText(text.toLowerCase()); props.showAlert("success", "Text Converted to lowercase");}

    const handleTitleCaseClick=()=>{
        let mywords = text.split(' ');
        let result = "";
        mywords.forEach(element => {
            result = result + element.charAt(0).toUpperCase() + element.slice(1).toLowerCase() + " ";
        });
        setText(result.trimEnd());
    }
    const handleClear=()=>{setText(''); props.showAlert("warning","Text has been Cleared");}
    const handleCopy=()=>{navigator.clipboard.writeText(text); props.showAlert("success", "Text Copied to Clipboard");}
    const handleCut=()=>{navigator.clipboard.writeText(text); setText('');}
    const handleExtraSpaces=()=>{let result = text.split(/[  ]+/); setText(result.join(' '));}
    
    const [text, setText] = useState('');
    return (
        <>
            <div className='container'>
                <h1>{props.heading}</h1>
                <div className="mb-3">
                    <textarea className={`form-control text-${props.theme.mode==='dark'?'light':'dark'}`} value={text} style={props.theme} onChange={handleOnChange} id="myBox" rows="8"></textarea>
                </div>
                <span className='container p-0'>
                    <button className="btn btn-dark m-1" onClick={handleClear}>Clear</button>
                    <button className="btn btn-dark m-1" onClick={handleCopy}>Copy</button>    
                    <button className="btn btn-dark m-1" onClick={handleCut}>Cut</button> 
                </span>
                <span className="container p-2 CaseConversion">
                    {/* <h3 className='m-2 mt-3'>Case Converter</h3> */}
                    <button className="btn btn-primary m-1" onClick={handleUpClick}>to UPPERCASE</button>
                    <button className="btn btn-primary m-2" onClick={handleLowClick}>to lowercase</button>
                    <button className="btn btn-primary m-1" onClick={handleTitleCaseClick}>to Titlecase</button>
                </span>
                <span className='container p-0'>
                    <button className="btn btn-success m-1" onClick={handleExtraSpaces}>Remove Extra Spaces</button>    
                </span>
            </div>
            
            <div className="container my-4">
                <h2>Your Text Summary</h2>
                <p>{text==='' ? 0:text.trim().split(/[  ]+/).length} words and {text.length} characters</p>
            </div>
            <div className="container my-3">
                <h2>Preview</h2>
                <p>{text}</p>
            </div>
        </>
    )
}