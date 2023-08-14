% Identify Neurons in a Mouse Brain Slice

% learn: imshow, alphadata, bwconncomp

%% 
clear
img = imread('100048576_197.jpg');
figure(1),clf
imshow(img)

% cut out the intrested section
img = squeeze(mean( img(1073:2335,2180:3803,:) ,3));

imagesc(img)
colormap gray
axis image

%% find appropriate threshold
figure(2), clf
hist(img(:),500)

thresh = 190;

% create a binarized thresholded map
threshmap = img < thresh; 

% get information about the 'islands' in the map

units = bwconncomp(threshmap);

figure(3),clf
imagesc(img), hold on
contour(threshmap,1,'r')
axis image
colormap gray

% remove if too small
unitsizes = cellfun(@length,units.PixelIdxList);

figure(4),clf
hist(unitsizes,900)
set(gca,'xlim',[0 250])
xlabel('Unit size'), ylabel('Count')

%select a pixel threshold
pixthresh = 8;

% now have to reconstruct a threshmap
threshmapFilt = false(size(threshmap));
for ui = 1:units.NumObjects
    
    % skip this unit if too small
    if unitsizes(ui) < pixthresh
        continue;
    end

    threshmapFilt(units.PixelIdxList{ui}) = 1;
end


figure(3),hold on
contour(threshmapFilt,1,'b','linew',2)



%% bonus

%color clusters according to size
sizecolormap = nan(size(img));
for ui=1:units.NumObjects
    sizecolormap(units.PixelIdxList{ui}) = log(unitsizes(ui)); 
end

%create alpha map (transparency)
alphamap = ones(size(img));
alphamap( ~isfinite(sizecolormap)) = 0;

figure(5), clf
imagesc(sizecolormap, 'Alphadata' ,alphamap)
set(gca,'clim',[0 7])













