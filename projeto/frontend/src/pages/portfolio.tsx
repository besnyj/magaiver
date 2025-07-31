import React, { useState } from 'react';
import {
    Button,
    Container,
    Typography,
    Box,
    CircularProgress,
    Alert,
    AlertTitle
} from '@mui/material';
import { styled } from '@mui/material/styles';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

const VisuallyHiddenInput = styled('input')({
    clip: 'rect(0 0 0 0)',
    clipPath: 'inset(50%)',
    height: 1,
    overflow: 'hidden',
    position: 'absolute',
    bottom: 0,
    left: 0,
    whiteSpace: 'nowrap',
    width: 1,
});

export default function Portfolio(): React.ReactElement {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [isUploading, setIsUploading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);
    const [apiResponse, setApiResponse] = useState<string | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0];
        if (file && (file.type === 'application/vnd.ms-excel' || file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')) {
            setSelectedFile(file);
        } else {
            setSelectedFile(null);
            setError("Please select a valid Excel file (.xls, .xlsx).");
        }
    };

    const handleReset = () => {
        setSelectedFile(null);
        setIsUploading(false);
        setError(null);
        setApiResponse(null);
    };

    const handleSubmit = async () => {
        if (!selectedFile) {
            setError("No file selected.");
            return;
        }

        setIsUploading(true);
        setError(null);
        setApiResponse(null);

        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await fetch('http://localhost:8000/upload_overview', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.message || 'Something went wrong');
            }

            setApiResponse(data.message || 'Upload successful!');

        } catch (err: any) {
            setError(err.message || 'Failed to upload file.');
        } finally {
            setIsUploading(false);
        }
    };

    if (apiResponse || error) {
        return (
            <Container maxWidth="sm">
                <Box sx={{ mt: 8, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 3 }}>
                    {apiResponse && (
                        <Typography component="h2" dangerouslySetInnerHTML={{__html: apiResponse}}>
                        </Typography>
                    )}
                    {error && (
                        <Alert severity="error" sx={{ width: '100%', textAlign: 'left' }}>
                            <AlertTitle>Error</AlertTitle>
                            {error}
                        </Alert>
                    )}
                    <Button variant="contained" onClick={handleReset}>
                        {apiResponse ? 'Upload Another File' : 'Try Again'}
                    </Button>
                </Box>
            </Container>
        );
    }


    return (
        <Container maxWidth="sm">
            <Box
                sx={{
                    mt: 20,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: 2,
                }}
            >
                <Button
                    component="label"
                    role={undefined}
                    variant="contained"
                    tabIndex={-1}
                    startIcon={<CloudUploadIcon />}
                    disabled={isUploading}
                >
                    Selecione um Overview
                    <VisuallyHiddenInput
                        type="file"
                        onChange={handleFileChange}
                        accept=".xlsx, .xls"
                    />
                </Button>

                <Typography variant="body1">
                    {selectedFile ? `File: ${selectedFile.name}` : "Nenhum overview selecionado"}
                </Typography>

                <Box sx={{ height: 40, position: 'relative' }}>
                    {!isUploading ? (
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleSubmit}
                            disabled={!selectedFile || isUploading}
                        >
                            Enviar
                        </Button>
                    ) : (
                        <CircularProgress />
                    )}
                </Box>
            </Box>
        </Container>
    );
}