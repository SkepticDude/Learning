import React, {useState} from 'react'

export default function TextForm(props) {
    const handleOnChange = (event) => {
        setText(event.target.value);
    }
    const handleUpClick=()=>{
        setText(text.toUpperCase());
    }
    const handleLowClick=()=>{
        setText(text.toLowerCase());
    }
    const handleTitleCaseClick=()=>{
        let mywords = text.split(' ');
        let result = "";
        mywords.forEach(element => {
            result = result + element.charAt(0).toUpperCase() + element.slice(1).toLowerCase() + " ";
        });
        setText(result.trimEnd());
    }


    const [text, setText] = useState('');
    return (
        <>
            <div className='container'>
                <h1>{props.heading}</h1>
                <div className="mb-3">
                    <textarea className="form-control" value={text} onChange={handleOnChange} id="myBox" rows="8"></textarea>
                </div>
                <button className="btn btn-primary mx-1" onClick={handleUpClick}>to UpperCase</button>
                <button className="btn btn-primary mx-1" onClick={handleLowClick}>to LowerCase</button>
                <button className="btn btn-primary mx-1" onClick={handleTitleCaseClick}>to TitleCase</button>

            </div>
            <div className="container my-4">
                <h2>Your Text Summary</h2>
                <p>{text.split(" ").length} words and {text.length} characters</p>
            </div>
            <div className="container my-3">
                <h2>Preview</h2>
                <p>{text}</p>
            </div>
        </>
    )
}