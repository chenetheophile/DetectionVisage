import { Subject } from 'rxjs';
import { PdfLayer } from './options/optional_content_config';
import { PDFPrintRange } from './options/pdf-print-range';
export interface FindOptions {
    highlightAll?: boolean;
    matchCase?: boolean;
    wholeWords?: boolean;
    ignoreAccents?: boolean;
    findMultipleSearchTexts?: boolean;
    fuzzySearch?: boolean;
    currentPage?: boolean;
    pageRange?: string;
}
export interface PDFExportScaleFactor {
    width?: number;
    height?: number;
    scale?: number;
}
export declare class NgxExtendedPdfViewerService {
    recalculateSize$: Subject<void>;
    findMultiple(text: Array<string>, options?: FindOptions): boolean;
    find(text: string, options?: FindOptions): boolean;
    findNext(): boolean;
    findPrevious(): boolean;
    print(printRange?: PDFPrintRange): void;
    removePrintRange(): void;
    setPrintRange(printRange: PDFPrintRange): void;
    filteredPageCount(pageCount: number, range: PDFPrintRange): number;
    isInPDFPrintRange(pageIndex: number, printRange: PDFPrintRange): boolean;
    getPageAsText(pageNumber: number): Promise<string>;
    private convertTextInfoToText;
    getPageAsImage(pageNumber: number, scale: PDFExportScaleFactor, background?: string, backgroundColorToReplace?: string): Promise<any>;
    private draw;
    private getPageDrawContext;
    getCurrentDocumentAsBlob(): Promise<Blob>;
    getFormData(currentFormValues?: boolean): Promise<Array<Object>>;
    /**
     * Adds a page to the rendering queue
     * @param {number} pageIndex Index of the page to render
     * @returns {boolean} false, if the page has already been rendered
     * or if it's out of range
     */
    addPageToRenderQueue(pageIndex: number): boolean;
    isRenderQueueEmpty(): boolean;
    hasPageBeenRendered(pageIndex: number): boolean;
    currentlyRenderedPages(): Array<number>;
    numberOfPages(): number;
    getCurrentlyVisiblePageNumbers(): Array<number>;
    recalculateSize(): void;
    listLayers(): Promise<Array<PdfLayer> | undefined>;
    toggleLayer(layerId: string): Promise<void>;
    scrollPageIntoView(pageNumber: number, pageSpot?: {
        top?: number | string;
        left?: number | string;
    }): void;
}
