export interface PdfBackgroundParameters {
    pageNumber?: number;
    pageLabel?: number;
    context?: CanvasRenderingContext2D;
    width?: number;
    height?: number;
}
export declare type PdfBackgroundAlgorithm = (params: PdfBackgroundParameters) => string | void;
export declare type PdfBackground = string | PdfBackgroundAlgorithm | undefined;
