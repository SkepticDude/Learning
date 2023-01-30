import React from 'react'

export default function Alert(props) {
  return ( props.alert &&
    <div className={`alert alert-${props.alert.type.toLowerCase()}`} role="alert">
        <strong>{Capitalize(props.alert.type)}</strong> : {props.alert.msg}
    </div>
  )
}

const Capitalize = (mystr) => mystr.charAt(0).toUpperCase() + mystr.slice(1).toLowerCase();