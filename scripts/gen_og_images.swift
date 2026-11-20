// Renders CMO-approved 1200x630 social preview cards with real system text.
// Usage: swift scripts/gen_og_images.swift <manifest.json> <output-dir>
// No network, no AI-generated text, no client proof, no prices on demo cards.
import Foundation
import AppKit

struct Card: Decodable {
    let out: String
    let kicker: String
    let title: String
    let sub: String
    let chip: String
    let accent: String
    let accent2: String
    let demo: Bool
}

let args = CommandLine.arguments
guard args.count >= 3 else {
    fputs("usage: gen_og_images.swift <manifest.json> <output-dir>\n", stderr)
    exit(2)
}
let manifest = URL(fileURLWithPath: args[1])
let outDir = URL(fileURLWithPath: args[2])
try FileManager.default.createDirectory(at: outDir, withIntermediateDirectories: true)
let cards = try JSONDecoder().decode([Card].self, from: Data(contentsOf: manifest))

let W: CGFloat = 1200
let H: CGFloat = 630

// Layout is expressed in top-left coordinates; AppKit bitmap contexts use bottom-left.
func rectTop(_ x: CGFloat, _ top: CGFloat, _ w: CGFloat, _ h: CGFloat) -> NSRect {
    NSRect(x: x, y: H - top - h, width: w, height: h)
}
func pointTop(_ x: CGFloat, _ top: CGFloat, _ text: NSString, _ attrs: [NSAttributedString.Key: Any]) -> NSPoint {
    NSPoint(x: x, y: H - top - text.size(withAttributes: attrs).height)
}

func color(_ hex: String) -> NSColor {
    let s = hex.trimmingCharacters(in: CharacterSet(charactersIn: "#"))
    guard s.count == 6,
          let r = Int(String(s.prefix(2)), radix: 16),
          let g = Int(String(s.dropFirst(2).prefix(2)), radix: 16),
          let b = Int(String(s.suffix(2)), radix: 16) else { return .systemIndigo }
    return NSColor(calibratedRed: CGFloat(r) / 255, green: CGFloat(g) / 255, blue: CGFloat(b) / 255, alpha: 1)
}

func wrap(_ text: String, font: NSFont, maxWidth: CGFloat) -> [String] {
    var lines: [String] = []
    for raw in text.components(separatedBy: "\n") {
        var line = ""
        for word in raw.split(separator: " ") {
            let candidate = line.isEmpty ? String(word) : line + " " + word
            let width = (candidate as NSString).size(withAttributes: [.font: font]).width
            if width <= maxWidth || line.isEmpty {
                line = candidate
            } else {
                lines.append(line)
                line = String(word)
            }
        }
        lines.append(line)
    }
    return lines
}

for card in cards {
    let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(W), pixelsHigh: Int(H),
                               bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                               colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
    NSGraphicsContext.saveGraphicsState()
    let context = NSGraphicsContext(bitmapImageRep: rep)!
    NSGraphicsContext.current = context

    NSColor(calibratedRed: 0.055, green: 0.07, blue: 0.13, alpha: 1).setFill()
    NSRect(x: 0, y: 0, width: W, height: H).fill()

    let c1 = color(card.accent)
    let c2 = color(card.accent2)
    c2.withAlphaComponent(0.30).setFill()
    NSBezierPath(ovalIn: rectTop(810, -150, 540, 540)).fill()
    c1.withAlphaComponent(0.24).setFill()
    NSBezierPath(ovalIn: rectTop(-170, 350, 540, 540)).fill()
    c1.setFill()
    NSRect(x: 0, y: 0, width: 14, height: H).fill()

    let brandFont = NSFont.boldSystemFont(ofSize: 30)
    let brandAttrs: [NSAttributedString.Key: Any] = [.font: brandFont, .foregroundColor: NSColor.white]
    (card.kicker as NSString).draw(at: pointTop(80, 62, card.kicker as NSString, brandAttrs),
                                   withAttributes: brandAttrs)

    if card.demo {
        let chipFont = NSFont.boldSystemFont(ofSize: 17)
        let chip = "CONCEPT DEMO — NOT CLIENT WORK" as NSString
        let attrs: [NSAttributedString.Key: Any] = [.font: chipFont, .foregroundColor: NSColor.white]
        let tw = chip.size(withAttributes: attrs).width
        let pad: CGFloat = 16
        let rect = rectTop(W - 80 - (tw + pad * 2), 52, tw + pad * 2, 42)
        NSColor.white.withAlphaComponent(0.13).setFill()
        NSBezierPath(roundedRect: rect, xRadius: 21, yRadius: 21).fill()
        chip.draw(at: NSPoint(x: rect.origin.x + pad, y: rect.origin.y + 11), withAttributes: attrs)
    }

    let titleFont = NSFont.boldSystemFont(ofSize: 58)
    let paragraph = NSMutableParagraphStyle()
    paragraph.lineSpacing = 6
    let titleAttrs: [NSAttributedString.Key: Any] = [
        .font: titleFont, .foregroundColor: NSColor.white, .paragraphStyle: paragraph
    ]
    var top: CGFloat = card.demo ? 178 : 158
    for line in wrap(card.title, font: titleFont, maxWidth: 1040) {
        let l = line as NSString
        l.draw(at: pointTop(80, top, l, titleAttrs), withAttributes: titleAttrs)
        top += 70
    }
    top += 14

    let subFont = NSFont.systemFont(ofSize: 27, weight: .regular)
    let subAttrs: [NSAttributedString.Key: Any] = [
        .font: subFont, .foregroundColor: NSColor(calibratedWhite: 0.82, alpha: 1)
    ]
    for line in wrap(card.sub, font: subFont, maxWidth: 1020) {
        let l = line as NSString
        l.draw(at: pointTop(80, top, l, subAttrs), withAttributes: subAttrs)
        top += 38
    }

    let chipFont = NSFont.boldSystemFont(ofSize: 21)
    let chip = card.chip as NSString
    let attrs: [NSAttributedString.Key: Any] = [.font: chipFont, .foregroundColor: NSColor.white]
    let tw = chip.size(withAttributes: attrs).width
    let rect = rectTop(80, H - 100, tw + 44, 54)
    c1.withAlphaComponent(0.34).setFill()
    NSBezierPath(roundedRect: rect, xRadius: 27, yRadius: 27).fill()
    chip.draw(at: NSPoint(x: 102, y: rect.origin.y + 14), withAttributes: attrs)

    NSGraphicsContext.restoreGraphicsState()
    let png = rep.representation(using: .png, properties: [:])!
    try png.write(to: outDir.appendingPathComponent(card.out))
    print("wrote \(card.out) (\(png.count) bytes)")
}
