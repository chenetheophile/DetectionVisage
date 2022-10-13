import { PDFNotificationService } from './../../pdf-notification-service';
import { UpdateUIStateEvent } from '../../events/update-ui-state-event';
import * as i0 from "@angular/core";
export declare class PdfRotatePageComponent {
    private notificationService;
    showRotateButton: boolean;
    disableRotate: boolean;
    clockwise: boolean;
    counterClockwise: boolean;
    private button1;
    private button2;
    constructor(notificationService: PDFNotificationService);
    rotateCW(): void;
    rotateCCW(): void;
    onPdfJsInit(): void;
    updateUIState(event: UpdateUIStateEvent): void;
    static ɵfac: i0.ɵɵFactoryDeclaration<PdfRotatePageComponent, never>;
    static ɵcmp: i0.ɵɵComponentDeclaration<PdfRotatePageComponent, "pdf-rotate-page", never, { "showRotateButton": "showRotateButton"; "clockwise": "clockwise"; "counterClockwise": "counterClockwise"; }, {}, never, never>;
}
