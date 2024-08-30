import * as MUI from '@mui/material';
import React from 'react';

import CSVType from './csvtype';

function Cell({person,day,defaultvalue}:{person:string,day:string,defaultvalue:string}){
    return (
        <MUI.TableCell>
            <input type="text" defaultValue={defaultvalue}/>
        </MUI.TableCell>
    );
}

function Row({person}:{person:CSVType}){
    return (
        <MUI.TableRow>
            {person && Object.keys(person).map(function(key:string){
                return (<Cell key={key} person={person['person']} day={key} defaultvalue={person[key]}/>);
            })}
        </MUI.TableRow>
    );
}

function Body(persons:CSVType[]){
    return (
        <MUI.TableBody>
            {persons.map(function(person:CSVType){
                return (
                    <Row key={person['person']} person={person}/>
                ); 
            })}
        </MUI.TableBody>
    );
}

function Heads(person:CSVType){
    return (
        <MUI.TableHead>
            <MUI.TableRow>
                {person && Object.keys(person).map(function(key:string){
                    return (
                        console.log(key),
                        <MUI.TableCell key={key}>{key}</MUI.TableCell>
                    );
                })}
            </MUI.TableRow>
        </MUI.TableHead>
    );
}

export default function Table(){
    async function Persons(){
        const options = {
          method: 'GET',
          headers: {'Content-Type': 'application/json'},
        };
        const data_josn = await fetch(`http://localhost:3000/api`,options).then(function(response){return response.json();})
        const data = data_josn['csvdata'];
        const persons = data.filter(function(person:CSVType){
            return person && person['person'];
        });
        console.log(persons);
        return persons;
    }
    return (
        <MUI.TableContainer>
            <MUI.Table>
                {Persons().then(function(persons:CSVType[]){
                    return (
                        <>
                            <Heads person={persons[1]}/>
                            {/* <Body persons={persons}/> */}
                        </>
                    );
                })}
            </MUI.Table>
        </MUI.TableContainer>
    );
}