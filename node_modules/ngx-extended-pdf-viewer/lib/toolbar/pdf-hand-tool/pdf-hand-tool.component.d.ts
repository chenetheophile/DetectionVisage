import { PDFNotificationService } from '../../pdf-notification-service';
import * as i0 from "@angular/core";
export declare class PdfHandToolComponent {
    private notificationService;
    showHandToolButton: boolean;
    isSelected: boolean;
    constructor(notificationService: PDFNotificationService);
    private onPdfJsInit;
    onClick(): void;
    static ɵfac: i0.ɵɵFactoryDeclaration<PdfHandToolComponent, never>;
    static ɵcmp: i0.ɵɵComponentDeclaration<PdfHandToolComponent, "pdf-hand-tool", never, { "showHandToolButton": "showHandToolButton"; }, {}, never, never>;
}
