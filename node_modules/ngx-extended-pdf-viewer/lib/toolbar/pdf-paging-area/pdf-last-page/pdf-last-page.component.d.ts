import { PDFNotificationService } from './../../../pdf-notification-service';
import { UpdateUIStateEvent } from '../../../events/update-ui-state-event';
import * as i0 from "@angular/core";
export declare class PdfLastPageComponent {
    private notificationService;
    disableLastPage: boolean;
    private button;
    constructor(notificationService: PDFNotificationService);
    firstPage(): void;
    onPdfJsInit(): void;
    updateUIState(event: UpdateUIStateEvent): void;
    lastPage(): void;
    static ɵfac: i0.ɵɵFactoryDeclaration<PdfLastPageComponent, never>;
    static ɵcmp: i0.ɵɵComponentDeclaration<PdfLastPageComponent, "pdf-last-page", never, {}, {}, never, never>;
}
