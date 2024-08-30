import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';
import Papa from 'papaparse';

import CSVType from '../csvtype';

export async function CSVData(csvFilePath:string) : Promise<CSVType[]> {
    const csvFile = await fs.readFile(csvFilePath, 'utf-8');
    let csvData : CSVType[] = [];
    Papa.parse(csvFile, {
        header: true,
        complete: function(result){csvData = result.data as CSVType[];}
    });
    return csvData; 
}

export async function GET(request: NextRequest) {
    const csvFilePath = path.join(process.cwd(), 'nextweek.csv');
    const csvdata :CSVType[]= await CSVData(csvFilePath);
    const { searchParams } = new URL(request.url);
    const person = searchParams.get('person');
    const day = searchParams.get('day') as keyof CSVType;
    const value = searchParams.get('value');
    if (!person || value) {
        return NextResponse.json({ csvdata });
    }
    const row: CSVType = csvdata.find(function(r){return r['person'] === person;}) as CSVType;
    if (!day) {
        return NextResponse.json({ row });
    }
    const cell = row[day];
    return NextResponse.json({ cell });
}

export async function POST(request: NextRequest) {
    const csvFilePath = path.join(process.cwd(), 'nextweek.csv');
    const csvdata :CSVType[]= await CSVData(csvFilePath);
    const { searchParams } = new URL(request.url);
    const person = searchParams.get('person');
    const day = searchParams.get('day') as keyof CSVType;
    const value = searchParams.get('value') as string;
    const NewCsvData = csvdata.map(function(r){
        if(r.person === person){
            r[day] = value;
        }
        return r;
    });
    const updatedCsv = Papa.unparse(NewCsvData, { header: true });
    await fs.writeFile(csvFilePath, updatedCsv, 'utf-8');
    return NextResponse.json({ success: true });
}