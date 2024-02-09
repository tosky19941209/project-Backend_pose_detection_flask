import React, { useState } from "react";
import api from '../service/axios.js';
import { Buffer } from "buffer";

function Track () {
  
  const [selectImg, setSelectImg] = useState(null)
  const [image_Upload_URL , setImage_Upload_Url] = useState(null)
  const [image_Result_URL , setImage_Result_Url] = useState(null)

  const handleImgChange = (e) => {
    setSelectImg(e.target.files[0])
    const img_up_url = URL.createObjectURL(e.target.files[0]);
    // console.log("url : " + img_up_url)
    setImage_Upload_Url(img_up_url)
  }

  const sendImgAnalysis = (e) => {
    const formdata = new FormData()
    console.log(selectImg)
    formdata.append('image',selectImg);
    api.post('upload', formdata, {
      headers: {
          'Content-Type': 'multipart/form-data'
      }
    })
    .then(res => {
      setImage_Result_Url(`data:image/jpeg;base64, ${res.data.image}`)
    })
    .catch((err) => {
      console.log("failed: " + err)
    })
  }



  return(
    <>
      <p style={{
        fontSize:"100px",
        color:"Yellow",
      }}>
        Pose Detection
      </p>
      <div className="flex mt-1">
        <img src = {image_Upload_URL} 
        style = {{
          width : '500px',
          height : "500px",
          marginLeft: '10px',
          marginRight: '10px'
        }}>
        </img>

        <img style={{
          width : "500px",
          height : "500px",
          marginLeft: '10px',
          marginRight: '10px'
        }} src = {image_Result_URL}></img>
      </div>

      <input type="file" onChange={handleImgChange}/>
      
      <button 
        onClick={ sendImgAnalysis }
        className="btn btn-info"
        style={{width:"400px", height:"100px", marginTop:"100px"}}>
          <p style={{fontSize:"50px", color:"red"}}>Pose Detect</p>
      </button>
    </>
  )
}

export default Track