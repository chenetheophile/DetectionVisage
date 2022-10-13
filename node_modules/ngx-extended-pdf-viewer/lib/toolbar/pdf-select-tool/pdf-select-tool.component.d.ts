import { PDFNotificationService } from '../../pdf-notification-service';
import * as i0 from "@angular/core";
export declare class PdfSelectToolComponent {
    private notificationService;
    showSelectToolButton: boolean;
    isSelected: boolean;
    constructor(notificationService: PDFNotificationService);
    private onPdfJsInit;
    onClick(): void;
    static ɵfac: i0.ɵɵFactoryDeclaration<PdfSelectToolComponent, never>;
    static ɵcmp: i0.ɵɵComponentDeclaration<PdfSelectToolComponent, "pdf-select-tool", never, { "showSelectToolButton": "showSelectToolButton"; }, {}, never, never>;
}
