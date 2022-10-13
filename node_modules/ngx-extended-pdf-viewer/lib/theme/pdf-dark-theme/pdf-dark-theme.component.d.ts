import { OnDestroy, OnInit, Renderer2 } from '@angular/core';
import * as i0 from "@angular/core";
export declare class PdfDarkThemeComponent implements OnInit, OnDestroy {
    private renderer;
    private document;
    constructor(renderer: Renderer2, document: any);
    ngOnInit(): void;
    private injectStyle;
    ngOnDestroy(): void;
    static ɵfac: i0.ɵɵFactoryDeclaration<PdfDarkThemeComponent, never>;
    static ɵcmp: i0.ɵɵComponentDeclaration<PdfDarkThemeComponent, "pdf-dark-theme", never, {}, {}, never, never>;
}
