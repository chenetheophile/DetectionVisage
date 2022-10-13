import { OptionalContentConfig } from './optional_content_config';
export declare enum ScrollModeType {
    vertical = 0,
    horizontal = 1,
    wrapped = 2,
    page = 3
}
export declare enum SpreadModeType {
    UNKNOWN = -1,
    NONE = 0,
    ODD = 1,
    EVEN = 2
}
export declare type PageViewModeType = 'single' | 'book' | 'multiple' | 'infinite-scroll';
export interface ScrollModeChangedEvent {
    mode: ScrollModeType;
}
export interface IPDFRenderingQueue {
    getHighestPriority(visiblePage: Array<any>, pages: Array<any>, scrolledDown: boolean, preRenderExtra: boolean): any;
}
export interface IPDFViewer {
    currentPageLabel: string | undefined;
    currentPageNumber: number;
    currentScaleValue: string | number;
    pagesRotation: 0 | 90 | 180 | 270;
    removePageBorders: boolean;
    renderingQueue: IPDFRenderingQueue;
    scrollMode: ScrollModeType;
    spreadMode: 0 | 1 | 2;
    _pages: Array<any>;
    addPageToRenderQueue(pageIndex: number): boolean;
    _getVisiblePages(): Array<any>;
    optionalContentConfigPromise: Promise<OptionalContentConfig> | null;
    _scrollPageIntoView({ pageDiv: HTMLElement, pageSpot: any, pageNumber: number }: {
        pageDiv: any;
        pageSpot: any;
        pageNumber: any;
    }): void;
}
