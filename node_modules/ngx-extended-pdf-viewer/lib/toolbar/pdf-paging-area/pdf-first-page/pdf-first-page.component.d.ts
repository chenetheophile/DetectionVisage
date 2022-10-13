import { PDFNotificationService } from './../../../pdf-notification-service';
import { UpdateUIStateEvent } from '../../../events/update-ui-state-event';
import * as i0 from "@angular/core";
export declare class PdfFirstPageComponent {
    private notificationService;
    disableFirstPage: boolean;
    private button;
    constructor(notificationService: PDFNotificationService);
    firstPage(): void;
    onPdfJsInit(): void;
    updateUIState(event: UpdateUIStateEvent): void;
    static ɵfac: i0.ɵɵFactoryDeclaration<PdfFirstPageComponent, never>;
    static ɵcmp: i0.ɵɵComponentDeclaration<PdfFirstPageComponent, "pdf-first-page", never, {}, {}, never, never>;
}
