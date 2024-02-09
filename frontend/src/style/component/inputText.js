import React from "react";

const Input = (props) => {
    return (
        <input
            type="text"
            className="form-control"
            placeholder={props.placeholder}
            onChange={props.onChange}
            style={{
                color: 'black',
                // boxShadow: '0 0 10px black',
                border: '1px solid ',
                borderRadius: '5px',

                width: "78%",
                height: "50px",

                marginTop: `${props.mt}`,
                marginBottom: `${props.mb}`,
                marginLeft: `${props.ml}`,
                marginRight: `${props.mr}`,

                paddingTop: `${props.pt}`,
                paddingBottom: `${props.pb}`,
                paddingLeft: `${props.pl}`,
                paddingRight: `${props.pr}`
            }}>
        </input>
    )
}

export default Input;