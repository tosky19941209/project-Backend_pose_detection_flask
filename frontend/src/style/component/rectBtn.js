import React from "react";

const RectBtn = (props) => {

    return (
        <button
            type="button"
            className="btn btn-info text-md-center align-items-md-center justify-content-center fs-2"
            style={{
                width: "78%",
                height: '50px',

                border: "0px solid",
                color: "white",
                fontSize: "",

                marginTop: `${props.mt}`,
                marginBottom: `${props.mb}`,
                marginLeft: `${props.ml}`,
                marginRight: `${props.mr}`,

                paddingTop: `${props.pt}`,
                paddingBottom: `${props.pb}`,
                paddingLeft: `${props.pl}`,
                paddingRight: `${props.pr}`
            }}
            onClick={() => {
                props.onClick()
            }}>
            {props.text}
        </button>

    );
}
export default RectBtn;