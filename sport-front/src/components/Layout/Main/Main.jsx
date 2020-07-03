import React, {useState, useEffect} from 'react';
import service from '../../../services/test.service';
import { NavLink } from "react-router-dom";
import { Switch, Route } from 'react-router-dom'
import map from "lodash/map"

import TestHome from "./TestHome"
import TestPage from "./TestPage"
import TestDetail from "./TestDetail"
const Main = () => {
    const [massiv, setMassiv] = useState([])
    useEffect(() => { 
        service.getData()
        .then(response => {
            console.log(response)
            setMassiv(response.data)
        })
    }, [])
    return (
        <>
            <div>
            <NavLink to={`/`}>PI</NavLink>
            <NavLink to={`/testnav`}>ALL</NavLink>
            {map(massiv, (item,key) => {
                return <NavLink key={item.id} to={`/testnav/${item.id}`}>
                    {item.id}
                </NavLink>
                })
            }
            <Switch>
                <Route exact path="/" component={TestHome}/>
                <Route exact path="/testnav" component={TestPage}/>
                <Route path="/testnav/:id" component={TestDetail} />
            </Switch>
            </div>
        </>
    )
}
export default Main