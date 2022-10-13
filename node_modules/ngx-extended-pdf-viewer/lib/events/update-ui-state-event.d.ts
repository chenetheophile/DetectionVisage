export interface UpdateUIStateEvent {
    source: any;
    widget: 'SecondaryToolbar' | 'Toolbar';
    pageNumber: number;
    pagesCount: number;
    pageScaleValue?: number;
    pageScale?: number | string;
}
