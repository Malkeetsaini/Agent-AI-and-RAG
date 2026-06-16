import {
 useState
} from "react";

import axios from "axios";

export default function ImageSearch(){

 const [file,setFile] =
 useState(null);

 const upload =
 async()=>{

  const formData =
  new FormData();

  formData.append(
   "file",
   file
  );

  await axios.post(
   "http://localhost:8000/image-search",
   formData
  );
 };

 return (

  <div>

   <input
    type="file"
    onChange={(e)=>
     setFile(
      e.target.files[0]
     )
    }
   />

   <button
    onClick={upload}
   >
    Search
   </button>

  </div>

 );
}