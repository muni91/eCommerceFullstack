import React from 'react'

const Base = ({
    title = "My Title",
    description = "My description",
    className = "bg-dark text-white p-4",
    children = ""
}) => {
    return (
        <div>
            <div className="container-fluid">
                <div className="jumbotron bg-dark text-white text-center">
                    <h2 className="display-4">{title}</h2>
                    <p className="lead">{description}</p>
                </div>
                <div className={className}>{children}</div>
            </div>
            <footer className="footer">
                <div className="container-fluid  bg-success text-white text-center py-3 ">
                    <h4>if you got any questions</h4>
                    <button className="btn btn-warning btn-lg">contact us</button>
                    <div className="container">
                        <span className="text-blue">
                            An amazing chicken in kht
                        </span>
                    </div>
                </div>
            </footer>
        </div>
    )
}

export default Base;