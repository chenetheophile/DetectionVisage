import { NgZone } from '@angular/core';
export declare class PinchOnMobileSupport {
    private _zone;
    private viewer;
    private startX;
    private startY;
    private initialPinchDistance;
    private pinchScale;
    private boundOnViewerTouchStart;
    private boundOnViewerTouchMove;
    private boundOnViewerTouchEnd;
    constructor(_zone: NgZone);
    private isMobile;
    private onViewerTouchStart;
    private onViewerTouchMove;
    private onViewerTouchEnd;
    private resetPinchZoomParams;
    initializePinchZoom(): void;
    destroyPinchZoom(): void;
}
